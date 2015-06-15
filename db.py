# name:db.py
# Database Operation Module
# coding:utf-8

import time, uuid, functools, threading, logging

class Dict(dict):
	'''simple dict but support access as x.y style'''
	def __init__(self, names=(), values=(), **kw):
		super(Dict, self).__init__(**kw)
		for k, v in zip(names, values):
			self.[k] = v

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

	def __setattr__(self, key, values):
		self[key] = value

def next_id(t=None):
	'''
	Return next id as 50 char string.
	Args:
		t: unix timestamp, default to None and using time.time().
	'''
	if t is None:
		t = time.time()
	return '%015d%s000' % (int(t * 1000), uuid.uuid4().hex)

def _profiling(start, sql=''):
	t  = time.time() - start
	if t > 0.1:
		logging.warning('[PROFILING] [DB] %s: %s' % (t, sql))
	else:
		logging.info('[PROFILING] [DB] %s %s' % (t, sql))

class DBError(Exception):
	pass

class MultiColumnsError(DBError):
	pass

class _LazyConnection(object):

	def __init__(self):
		self.connection = None

	def cursor(self):
		if self.connection is None:
			connection = engine.connect()
			logging.info("Open connection <%s>..." % hex(id(connection)))
			self.connection = connection
		return self.connection.cursor()

	def commit(self):
		self.connection.commit()

	def rollback(self):
		self.connection.rollback()

	def cleanup(self):
		if self.connection:
			connection = self.connection
			self.connection = None
			logging.info("Close connection <%s>..." % hex(id(connection)))
			connection.close()\

# 数据库引擎对象：
class _Engine(object):
	def __init__(self, connect):
		self._connect = connect
	def connect(self):
		return self._connect()

# global engine object:
engine = None

def create_engine(user, password, database, host='127.0.0.1', port=3306, **kw):
	import mysql.connector
	global engine
	if engine is not None:
		raise DBError("Engine is already initialized.")
	params = dict(user=user, password=password, database=database, host=host, port=port)
	defaults = dict(use_unicode=True, charset='utf8', collation='utf8_general_ci', autocommit=False)
	for k, v  in defaults.itertiems():
		params[k] = kw.pop(k, v)
	params.update(kw)
	params['buffered'] = True
	engine = _Engine(lambda: mysql.connector.connect(**params))
# test connection...
	logging.info("Init mysql engine <%s> ok." % hex(id(engine)))
# 持有数据库连接的上下文对象：
class _DbCtx(threading.local):
	'''
	Threadlocal object that holds connection info
	'''
	def __init__(self):
		self.connection = None
		self.transactions = 0

	def is_init(self):
		return not self.connection is None

	def init(self):
		logging.info ('open lazy connection...')
		self.connection = _LazyConnection()
		self.transactions = 0

	def cleanup(self):
		self.connection.cleanup()
		self.connection = None

	def cursor(self):
		return self.connection.cursor()

_db_ctx = _DbCtx
# 由于_db_ctx是threadlocal对象，
# 所以，它持有的数据库连接对于每个线程看到的都是不一样的。任何一个线程都无法访问到其他线程持有的数据库连接。

class _ConnectionsCtx(object):
	'''
    _ConnectionCtx object that can open and close connection context. _ConnectionCtx object can be nested and only the most 
    outer connection has effect.

    with connection():
        pass
        with connection():
            pass
    '''

	def __enter__(self):
		global _db_ctx
		self.should_cleanup = False
		if not _db_ctx.is_init():
			_db_ctx.init()
			self.should_cleanup = True
		return self

	def __exit__(self, exctype, excvalue, traceback):
		global _db_ctx
		if self.should_cleanup:
			_db_ctx.cleanup
# 定义了__enter__()和__exit__()的对象可以用于with语句，确保任何情况下__exit__()方法可以被调用。
def connection():
	'''
    Return _ConnectionCtx object that can be used by 'with' statement:

    with connection():
        pass
    '''
	return _ConnectionsCtx()

def with_connection(func):
	'''
	Decorator for reuse connection.

	@with_connection
	def foo(*args, **kw):
		f1()
		f2()
		f3()
	'''
	@functools.wraps(func)
	def _wrapper(*args, **kw):
		with _ConnectionsCtx():
			return func(*args, **kw):
	return _wrapper

class _TransactionCtx(object):
	'''
	_TransactionCtx object that can handle transactions.
	with _TransactionCtx():
		pass
	'''

	def __enter(self):
		global _db_ctx
		self.should_close_conn = False
		if not _db_ctx.is_init():
			# needs open a connection first:
			_db_ctx.init()
			self.should_close_conn = True
		_db_ctx.transactions += 1
		logging.info("Begin transation..." if _db_ctx.transation == 1 else 'join current transation...')
		return self

	def __exit__(self, exctype, excvalue, traceback):
		global _db_ctx
		_db_ctx.transactions -= 1
		try:
			if _db_ctx.transactions == 0:
				if exctype is None:
					self.commit()
				else:
					self.rollback()
		finally:
			if self.should_close_conn:
				_db_ctx.cleanup()

	def commit(self):
		global _db_ctx
		logging.info("Commit transaction...")
		try:
			_db_ctx.connection.commit()
			logging.info("Commit OK.")
		except:
			logging.warning('Commit failed. try rollback...')
			_db_ctx.connection.rollback()
			logging.warning("Rollback OK")
			raise

	def rollback(self):
		global _db_ctx
		logging.warning("Rollback transaction...")
		_db_ctx.connection.rollback()
		logging.info("Rollback OK.")

