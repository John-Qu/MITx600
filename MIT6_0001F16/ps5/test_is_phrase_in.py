from ps5 import *

if __name__ == '__main__':
    cuddly = NewsStory('', 'The purple cow is soft and cuddly.', '', '', datetime.now())
    exclaim = NewsStory('', 'Purple!!! Cow!!!', '', '', datetime.now())
    plural = NewsStory('', 'Purple cows are cool!', '', '', datetime.now())
    s1 = TitleTrigger('PURPLE COW')
    s2 = TitleTrigger('purple cow')
    for trig in [s1, s2]:
        print(trig.evaluate(cuddly))
        print(trig.evaluate(exclaim))
        print(trig.evaluate(plural))

