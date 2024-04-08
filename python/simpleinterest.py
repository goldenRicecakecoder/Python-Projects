#Write a program to find the simple interest 
#for the given principle amount, 
#time and rate of interest

def simple_interest(p,t,r):
    print('The principal amount is ', p)
    print('The time period is ', t)
    print('The rate of interest is ', r)

    simpleInterest = (p * t * r)/100

    print('The simple interest is ', simpleInterest)
    return simpleInterest

simple_interest(8,6,8)