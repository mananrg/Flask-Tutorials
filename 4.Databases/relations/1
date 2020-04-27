from relations import db,Puppy,Owner,Toy
tom=Puppy('tom')
sam=Puppy('sam')

db.session.add_all([tom,sam])
db.session.commit()

print(Puppy.query.all())
manan=Owner("manan",tom.id)

toy1=Toy('toy1',tom.id)
toy2=Toy('toy2',tom.id)
toy3=Toy('toy3',tom.id)
db.session.add_all([manan,toy1,toy2,toy3])
db.session.commit()
print(tom.report_toys())
