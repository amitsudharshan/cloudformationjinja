import jinjatemplates as myjinja

if __name__ == '__main__':
    import os
    print myjinja.render("cloudtemplates/test.json", {})
