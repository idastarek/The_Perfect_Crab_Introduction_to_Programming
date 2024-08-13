# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

# print("")
# print("Function: report_long_words")

def report_long_words():
  words = ask_for_words()
  long_words = get_words_longer_than_ten(words)
  no_hyphen = remove_hyphen(long_words)
  too_long_words = shorten_words_longer_than_fiveteen(no_hyphen)
  report = create_report(too_long_words)
  return report

def ask_for_words():
  words = input("Please write 5 different words seperates by a comma: ")
  word_list = [word.strip() for word in words.split(',')]
  return word_list


def get_words_longer_than_ten(words):
  long_words = []
  for word in words:
    if len(word) > 10:
      long_words.append(word)
  return long_words

def remove_hyphen(long_words):
  no_hyphen = []
  for long_word in long_words:
    if '-' not in long_word:
      no_hyphen.append(long_word)
  return no_hyphen

def shorten_words_longer_than_fiveteen(no_hyphen):
  too_long_words = []
  for word in no_hyphen:
    if len(word) > 15:
       too_long_words.append(word[:15] + "...")
    else:
      too_long_words.append(word)
  return too_long_words


def create_report(too_long_words):
  results = too_long_words
  return "These words are quite long: " + ', '.join(results)


report = report_long_words()

print(report)


# check_that_these_are_equal(
#   report_long_words([
#     'hello',
#     'nonbiological',
#     'Kay',
#     'this-is-a-long-word',
#     'antidisestablishmentarianism'
#   ]),
#   "These words are quite long: nonbiological, antidisestablis..."
# )

# check_that_these_are_equal(
#   report_long_words([
#     'cat',
#     'dog',
#     'rhinosaurus',
#     'rhinosaurus-rex',
#     'frog'
#   ]),
#   "These words are quite long: rhinosaurus"
# )

# check_that_these_are_equal(
#   report_long_words([
#     'cat'
#   ]),
#   "These words are quite long: "
# )

# Once you're done, move on to 041_challenge_2_example.py


