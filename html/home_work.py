def check_password(password, chars = '$%!?@#'):
    step_1 = False
    for i in password:
        if i in chars:
            step_1 = True 
    if len(password) >= 8 and step_1 == True:
        return True
    else:
        return False
    
print(check_password('Ann@@@@@@'))

def html_test(text, tag = 'h1'):
    #"<h1>Hello Python</h1>"
    result = '<' + tag + '>' + text + '</' + tag + '>'
    return result

print(html_test('Hello Python'))
print(html_test('Hello Python', 'div'))