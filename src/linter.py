
def linter(config, filereader):
    print(filereader.getSheetnames())
    ws_form = filereader.getWorksheet('FORMS')
    rules = config.getRules()

    for rkey, rval in rules.items():
        print(rkey)
    