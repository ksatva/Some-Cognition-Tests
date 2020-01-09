# Some cognition tests

------
### 1. N-back test: to test short-term memory
    3 Difficulty levels 
        a. EASY (2-back) 
        b. MEDIUM (4-back) 
        c. HARD (5 back)

    A volunteer sees a computer screen where square boxes of different colors flashes for a moment one after other. The   volunteer needs to hit a key in keyboard when an n-back occurs. The program logs the response time and the correct/incorrect response. Multiple similar trials are recorded for each difficulty level.


### 2. Arithmetic test: to test working memory
    3 Difficulty levels 
        a. EASY (2 numbers) 
        b. MEDIUM (3 numbers) 
        c. HARD (5 numbers)

    A volunteer sees a computer screen where a number, an arithmatic operator, again a number appears alternately and finally a input form. The volunteer need to evaluate the result in mind and fill and submit the form. The program logs response time and the correct/incorrect response. Multiple similar trials are recorded for each difficulty level.

-----
## Running the tests
    (Preq.) A successful installation of expyriment module and necessary dependencies (see website link below)
    
    Note: In each directory there is a .py file starting with 'run_'
    Move to the corresponding test directory and run this file to start the test, eg. for 2 back test:
      $ python run_t1-L1.py

-----
The tests were designed with the python "expyriment" module "https://www.expyriment.org"
