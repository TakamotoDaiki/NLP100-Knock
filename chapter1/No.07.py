import string

def template(x, y, z):
    t_string = '$X時の$Yは$Z'
    Temp = string.Template(t_string)
    output = Temp.substitute(X=x, Y=y, Z=z)

    return output

def main():
    x = '12'
    y = '気温'
    z = '22.4'

    output = template(x, y, z)

    print(output)

if __name__ == '__main__':
    main()
    
