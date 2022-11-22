#Mohammad Abdul Gafoor
#21BCE9271

#Let the given boxes be A,B,C
def bayes_theorem(p_A, p_B, p_C,p_RA, p_RB, p_RC):
    # calculate Probability of red ball drawn is from B
    p_BR=(p_B*p_RB)/((p_A*p_RA)+(p_B*p_RB)+(p_C*p_RC))
    return p_BR
#Let P(A) be the probability of coosing a ball from box A
p_A = 1/3
#Let P(B) be the probability of coosing a ball from box B
p_B = 1/3
#Let P(C) be the probability of coosing a ball from box C
p_C = 1/3
#Let P(R) be the probability of getting a Red ball
#Let P(R/A) be the probability of getting a Red ball from Box A
p_RA = 3/5
#Let P(R/B) be the probability of getting a Red ball from Box B
p_RB = 4/9
#Let P(R/C) be the probability of getting a Red ball from Box C
p_RC = 2/6

result = bayes_theorem(p_A, p_B, p_C,p_RA, p_RB, p_RC)
# print result
print('P(B|R) = %.2f%%' % (result * 100))
