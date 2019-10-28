# nlp-for-email
homework 3 for machine learning class

P(ham/w) = P(w/ham) * P(ham) ignore the denominator 

P(w1/ham) = (# the words in the training list + 1) / (# words in the training list + nonrepeat words in the training list) 

In fact, I get log (P(w/ham))

For words that not appear in the traing list, the probability is, their probability  is the same: 

P(w2/ham) = (0 + 1) / (# words in the training list + nonrepeat words in the training list)

Until now, we have known all the necessay probability.

For different words, they are independent so the overall posterior probability in the test set: I just take one word w1 for example. 

sum ( w1_repeat times * log (P(w1/ham)) ) +  # words not appear in the train list * P(w2/ham)
