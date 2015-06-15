# more_function_run.py

import more_function

sentence = "All good things come to those who wait."

words = more_function.break_words(sentence)
print (words)

sorted_words = more_function.sort_words(words)
print (sorted_words)

more_function.print_first_word(words)
print (words)

more_function.print_last_word(words)
print (words)

more_function.print_first_word(sorted_words)
print (sorted_words)

more_function.print_last_word(sorted_words)
print (sorted_words)

sorted_words = more_function.sort_sentence(sentence)
print (sorted_words)

more_function.print_first_and_last(sentence)
print (sentence)

more_function.print_first_and_last_sorted(sentence)
print (sentence)
