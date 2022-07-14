# Function to identify person is eligible to vote

n = int(input("Please enter your age : "))


def eligible_to_vote(age):
    if age >= 18:
        print(" You are eligible to vote")
    else:
        print(" You are not eligible to vote")


eligible_to_vote(n)
