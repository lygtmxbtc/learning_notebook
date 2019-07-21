### create session
```bash
from sqlalchemy import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
sesson = Session()
```
### add & update
```bash
# insert one record
instance = Class(name='tm',age=27)
session.add(instance)
session.commit()

# insert many records
session.add_all([Class(),Class(),Class()])

# change record colume
instance.name = 'tmtc'

# record has been modified
session.dirty

# new class objects are pending
session.new
```
### query
```bash
query = session.query(Class).filter(Class.name.like('%tm')).order_by(Class.id)
query.all()
query.first()
query.one()
query.one_or_none()
query.scalar()

# use sql
from sqlalchemy import text
session.query(Class).filter(text("id<224")).all()

# with params
session.query(User).filter(text("id<:value and name=:name")).\
    params(value=224, name='fred').order_by(User.id).one()
    
# whole sql
session.query(User).from_statement(
                    text("SELECT * FROM users where name=:name")).\
                    params(name='ed').all()
                    
# counting
session.query(User).filter(User.name.like('%ed')).count()

from sqlalchemy import func
session.query(func.count(User.name), User.name).group_by(User.name).all()
```
### query with join
```bash
session.query(User).join(Address).\
        filter(Address.email_address=='jack@google.com').\
        all()
        
query.join(Address, User.id==Address.user_id)    # explicit condition
query.join(User.addresses)                       # specify relationship from left to right
query.join(Address, User.addresses)              # same, with explicit target
query.join('addresses')                          # same, using a string
```
### delete
```bash
session.delete(jack)

'''
if need delete the relation records
we’ll declare the User class, adding in the addresses relationship including the cascade configuration
'''
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    addresses = relationship("Address", back_populates='user',
                    cascade="all, delete, delete-orphan")

    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                               self.name, self.fullname, self.nickname)

```
### query API
https://docs.sqlalchemy.org/en/13/orm/query.html