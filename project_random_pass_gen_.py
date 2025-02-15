import random
import string

values=string.ascii_letters+ string.digits+string.punctuation
pass_len = 8
password ="".join ( [random.choice(values) for i  in range(pass_len)])
print(password)