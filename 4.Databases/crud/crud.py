from basicmodel import db,Puppy

#create 
my_puppy=Puppy('alpha',5)
db.session.add(my_puppy)
db.session.commit()

#read

#listing all the puppies
all_puppies=Puppy.query.all()
print(all_puppies)

#listing by id
firstpuppy=Puppy.query.get(1)
print(firstpuppy.name)
print(firstpuppy.age)

#filtering
pup_tom=Puppy.query.filter_by(name='tom')
print(pup_tom.all())


##update###
firstpuppy=Puppy.query.get(1)
firstpuppy.age=10
db.session.add(firstpuppy)
db.session.commit()
#delete##
secpuppy=Puppy.query.get(2)
db.session.delete(secpuppy)
db.session.commit()

all_puppies=Puppy.query.all()
print(all_puppies)

