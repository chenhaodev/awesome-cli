#!/usr/bin/env python
import os, sys

if len(sys.argv)>=2:
    if sys.argv[1] == '-h':
        print("translate the copied newsboat content and translate it into CN")
        print("step: 1. select and copy all content from newsboat (cmd+A, cmd+c)")
        print("step: 2. "+sys.argv[0])
        exit()

os.system('pbpaste > newsboat1.log')
os.system('tail -60 newsboat1.log > newsboat2.log')
filename = 'newsboat2.log'

with open(filename,'r') as f:
    lines = f.readlines()

out=''
ignore=['~','q:Quit s:Save n:Next Unread o:Open in Browser e:Enqueue']
ignore_header=['newsboat ', 'Link:']
ignore_on = 0
capture_on = 0

for line in lines:
    if line.find(ignore_header[0])!=-1 and ignore_on==0:
        ignore_on = 1
    if line.find(ignore_header[1])!=-1 and ignore_on==1:
        ignore_on = 0
        capture_on = 1
        continue
    if capture_on and line.find(ignore[0])==-1 and line.find(ignore[1])==-1: 
        out = out + line

#print(out)

with open(filename, 'w') as f:
    f.write(out)

os.system('trans -b :zh < newsboat2.log')
os.system('rm newsboat1.log')
os.system('rm newsboat2.log')

'''
Data format: 


newsboat 2.14.1 - Article 'Social Distancing Beliefs and Human Mobility: Evidence from Twitter. (arXiv:2008.04826v1 [cs.SI])' (7 unread, 10
Feed: cs updates on arXiv.org
Title: Social Distancing Beliefs and Human Mobility: Evidence from Twitter. (arXiv:2008.04826v1 [cs.SI])
Author: Simon Porcher,
href="http://arxiv.org/find/cs/1/au:+Renault_T/0/1/0/all/0/1">Thomas Renault
Date: Wed, 12 Aug 2020 21:10:36 +0800
Link: http://arxiv.org/abs/2008.04826

We construct a novel database containing hundreds of thousands geotagged messages related to the COVID-19 pandemic sent on Twitter. We
create a daily index of social distancing -- at the state level -- to capture social distancing beliefs by analyzing the number of
tweets containing keywords such as "stay home", "stay safe", "wear mask", "wash hands" and "social distancing". We find that an
increase in the Twitter index of social distancing on day t-1 is associated with a decrease in mobility on day t. We also find that
state orders, an increase in the number of COVID cases, precipitation and temperature contribute to reducing human mobility. Republican
states are also less likely to enforce social distancing. Beliefs shared on social networks could both reveal the behavior of
individuals and influence the behavior of others. Our findings suggest that policy makers can use geotagged Twitter data -- in
conjunction with mobility data -- to better understand individual voluntary social distancing actions.
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
q:Quit s:Save n:Next Unread o:Open in Browser e:Enqueue ?:Help                                                                        Top
'''
