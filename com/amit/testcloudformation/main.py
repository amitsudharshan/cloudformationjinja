import jinjatemplates as myjinja

if __name__ == '__main__':
    import os
    f = open("/Users/amit/dev/cftemplates/ec2.json", 'w')
    f.write(myjinja.render("cloudtemplates/test.json", {}))
    f.close()
