
large_file = "large.txt"



# # BAD: READS THE WHOLE FILE INTO MEMORY AT ONCE
# with open(large_file, "r") as f:
#     words = f.read().split()
#
# for word in words:
#     # Add your code here, eg. matching a pattern
#     print(word)


# Redo using generators
def words_in_file(path):
    with open(path, "r") as f:
        for line in f:
            for word in line.split():
                yield word

my_generator = words_in_file(large_file)
for word in my_generator:
    # Add your code here, eg. matching a pattern
    print(word)

