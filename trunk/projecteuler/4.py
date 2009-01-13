# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# FIXME: returns the correct answer for (99..9), but not (999..99)!  I don't
# know why yet.
def largest_palindrome():
    for i in range (999, 99, -1):
        for j in range (999, 99, -1):
            str_prod = str(i * j);
            str_prod_rev = ''.join(reversed(str_prod))
            if str_prod == str_prod_rev:
                print i, "*", j, "produces:"
                return str_prod

print largest_palindrome()