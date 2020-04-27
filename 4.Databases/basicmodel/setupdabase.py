from basicmodel import db,Puppy

#manually creating database
db.create_all()

rufus=Puppy('rufus',5)
tom=Puppy('tom',6)

print(rufus.id)
print(tom.id)
#adding rufus and tom to db together
db.session.add_all([rufus,tom])
#db.session.add(sam)
db.session.commit()
print(rufus.id)
print(tom.id)
