# DISCLAIMER
Detta är mitt (Hugos) formelblad när jag skrev tentan. Kan inte garantera att något är relevant (tror inte jag använde något härifrån själv) men det efterfrågades under ett pass.

# Formulas
## Lists and Dictionaries
### Convert entire list to singular datatype
```python
# Convert all items in a list to a singular datatype
def list_to_datatype(data: list, datatype: type) -> list:
	return [datatype(i) for i in data]
```
### Sorting nested list
```python 
# How to sort a nested list
# data is the list you want to sort
# byElement is the index inside of the inner list you want to sort by
# ascending is true if the list should be sorted from lowest to highest or reversed
def sort_nested_list(data: list, byElement: int, ascending: bool) -> list:
	if byElement > len(data[0])-1:
		return data
	return sorted(data, key=lambda x: x[byElement], reverse=(not ascending))
```
## Check if list is full of identical elements
```python
def check_if_identical(data: list) -> bool:
	# Removes duplicate objects in list by converting to mathemitical set
	# If length of set is 1, list is full of only identical items
	# Remember that a list full of NoneType objects returns True 
	return True if len(set(data)) == 1 else False 
```
### Converting Dictionary to nested list:
```python
data = {"A": 1, "B":2, "C":3}
convertedList = [[i, data[i]] for i in data]
# convertedList = [["A", 1], ["B", 2], ["C", 3]]
```
### Merge two dictionaries
```python
dict1 = { 'a': 1, 'b': 2 }
dict2 = { 'b': 3, 'c': 4 }
merged = { **dict1, **dict2 }
# {'a': 1, 'b': 3, 'c': 4}
```
## String manipulation
### Reversing a string
```python
reversed = original[::-1]
```
### Titling
```python
msg = "dark knight"
print(msg.title())
# Prints: Dark Knight
```
### Joining
```python
join_char = " "

msg = join_char.join(["Python", "Is", "Awesome"])
# msg = Python is Awesome
```
### Slicing
```python
msg = 'yellow'

msg[1] # => 'e' Takes second letter
msg[-1] # => 'w' Takes last letter
msg[4:6] # => 'ow' Includes 5th letter but does not include 7th letter
msg[:4] # => 'yell' # Includes every up to but not including the 5th letter
msg[-3:] # => 'low' # Takes the last 3 letters
```
# Matrices
## Transposing
```python
matrix = [[1,2,3], [4,5,6]]
transposed_matrix = list(zip(*mat))

# Converts the inner tuples created by zip to lists
for index, row in enumerate(transposed_matrix):
	transposed_matrix[index] = list(transposed_matrix[index])
```