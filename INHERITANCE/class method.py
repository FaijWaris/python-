class empolyee:
    a=1
    @classmethod# ye as a decoraaaaater use hota hai jb hme sirf class ke attribute ko dikhane rhta hai atb
    def show(cls):
        print(f" eployee class method{cls.a}")

e=empolyee()
e.a=23
e.show()