fh = open(("C:/Users/ast/work/edm1/edmbuild/edmcore_build_2017.all.out"), "r")

for line in fh:
    if (" error ") in line:
        #if not ("cs_errors" or "ei_xmlerror" or "") in line:
        print line

fh.close();
