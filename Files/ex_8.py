def save_applicant_data(source, output):
    text_out = []
    for i in source:
        list = [*i.values()]
        text = ','.join(str(e) for e in list)
        text_out.append(text+'\n')
    with open(output, 'w') as fh:
        fh.writelines(text_out)