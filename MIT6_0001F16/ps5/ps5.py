# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: John Qu
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    """
    Store the attributes in one object.
    - globally unique identifier (GUID) - a string
    - title - a string
    - description - a string
    - link to more content - a string
    - pubdate - a ​datetime
    """
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def is_phrase_in(self, text):
        separators = string.punctuation + string.whitespace
        new_text = text
        for cha in separators:
            new_text = new_text.replace(cha, ' ')
        words_list = new_text.split()
        words_in_text_list = list()
        for word in words_list:
            words_in_text_list.append(word.lower())
        words_in_text_string = ' ' + ' '.join(words_in_text_list) + ' '
        try:
            index = words_in_text_string.index(self.phrase)
            len_phrase = len(self.phrase)
            return words_in_text_string[index - 1] == ' ' \
                   and words_in_text_string[index + len_phrase] == ' '
        except ValueError:
            return False

    # def is_phrase_in(self, text):
    #     words_list = list(text)
    #     separators = string.punctuation + string.whitespace
    #     for index in range(len(separators)):
    #         words_temp = list()
    #         for word in words_list:
    #             words_temp += word.split(separators[index])
    #         words_list = words_temp
    #     words_in_text_list = list()
    #     for word in words_list:
    #         words_in_text_list.append(word.lower())
    #     words_in_text_string = ' '.join(words_in_text_list)
    #     return self.phrase in words_in_text_string

# Problem 3
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        """
        :param story: a NewsStory type object
        :return:
        """
        return self.is_phrase_in(story.get_title())

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        """
        :param story: a NewsStory type object
        :return: True if phrase is in description
        """
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS


# Problem 5
class TimeTrigger(Trigger):
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
    def __init__(self, trigger_time):
        trigger_time_dt = datetime.strptime(trigger_time, "%d %b %Y %H:%M:%S")
        trigger_time_dt = trigger_time_dt.replace(tzinfo=pytz.timezone("EST"))
        self.dt = trigger_time_dt


# Problem 6
class BeforeTrigger(TimeTrigger):
    def __init__(self, trigger_time_str):
        """
        :param time: string of datetime
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
        """
        TimeTrigger.__init__(self, trigger_time_str)

    def evaluate(self, story):
        try:
            return story.get_pubdate() < self.dt
        except TypeError:
            story_pubdate_aware = story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))
            return story_pubdate_aware < self.dt

class AfterTrigger(TimeTrigger):
    # def __init__(self, trigger_time_str):
    #     """
    #     :param time: string of datetime
    #     Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
    #     """
    #     TimeTrigger.__init__(self, trigger_time_str)

    def evaluate(self, story):
        try:
            return story.get_pubdate() >= self.dt
        except TypeError:
            story_pubdate_aware = story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))
            return story_pubdate_aware >= self.dt

# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, T):
        """
        invert the result of another trigger
        :param T: a trigger
        """
        self.invert_trigger = T

    def evaluate(self, story):
        return not self.invert_trigger.evaluate(story)


# Problem 8
class AndTrigger(Trigger):

    def __init__(self, T1, T2):
        """
        invert the result of another trigger
        :param T: a trigger
        """
        self.T1 = T1
        self.T2 = T2

    def evaluate(self, story):
        return self.T1.evaluate(story) and self.T2.evaluate(story)


# Problem 9
class OrTrigger(Trigger):

    def __init__(self, T1, T2):
        """
        invert the result of another trigger
        :param T: a trigger
        """
        self.T1 = T1
        self.T2 = T2

    def evaluate(self, story):
        return self.T1.evaluate(story) or self.T2.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    stories_unfiltered = stories.copy()
    for story in stories_unfiltered:
        story_fire = False
        for trigger in triggerlist:
            story_fire = story_fire or trigger.evaluate(story)
        if not story_fire:
            stories.remove(story)
    return stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    trigger_list = list()
    trigger_log = dict()
    for line in lines:
        messages = line.split(',')
        if messages[0] == 'ADD':
            for i in range(1, len(messages)):
                trigger_list.append(trigger_log[messages[i]])
        else:
            if messages[1] == 'TITLE':
                trigger_log[messages[0]] = TitleTrigger(messages[2])
            elif messages[1] == 'DESCRIPTION':
                trigger_log[messages[0]] = DescriptionTrigger(messages[2])
            elif messages[1] == 'AFTER':
                trigger_log[messages[0]] = AfterTrigger(messages[2])
            elif messages[1] == 'BEFORE':
                trigger_log[messages[0]] = BeforeTrigger(messages[2])
            elif messages[1] == 'AND':
                trigger_log[messages[0]] = AndTrigger(trigger_log[messages[2]], trigger_log[messages[3]])
            elif messages[1] == 'OR':
                trigger_log[messages[0]] = OrTrigger(trigger_log[messages[2]], trigger_log[messages[3]])
            elif messages[1] == 'NOT':
                trigger_log[messages[0]] = NotTrigger(trigger_log[messages[2]])
    return trigger_list

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        # t1 = TitleTrigger("election")
        # t2 = DescriptionTrigger("Trump")
        # t3 = DescriptionTrigger("Clinton")
        # t4 = AndTrigger(t2, t3)
        # triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    # root = Tk()
    # root.title("Some RSS parser")
    # t = threading.Thread(target=main_thread, args=(root,))
    # t.start()
    # root.mainloop()
    # story = NewsStory('', '', '', '', datetime.now())

    story = NewsStory('test guid', 'test title',
                  'test description', 'test link', datetime.now())
    print(story.get_guid() == 'test guid')
    print(story.get_title() == 'test title')
    print(story.get_description() == 'test description')
    print(story.get_link() == 'test link')
    print(type(story.get_pubdate()) == datetime)
    print("---")

    cuddly = NewsStory('', 'The purple cow is soft and cuddly.', '', '',
                   datetime.now())
    s1 = TitleTrigger('PURPLE COW')
    print(s1.evaluate(cuddly))

    cuddly = NewsStory('', '', 'The purple cow is soft and cuddly.', '',
                       datetime.now())
    s2 = DescriptionTrigger('PURPLE COW')
    print(s2.evaluate(cuddly))

    triggerlist = read_trigger_config('triggers.txt')
