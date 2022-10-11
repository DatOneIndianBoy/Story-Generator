import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 27th October']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
name = ['John', 'Cameron','Tim', 'Lisa', 'Bob']
residence = ['Sweden','India', 'Canada', 'America', 'England']
went = ['Bank', 'park','library', 'school', 'laundry']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mystery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
