def get_cases(txt:str) -> list:

    with open(txt) as f:
        lines = f.readlines()

    cases = []
    case = []

    for line in lines:
        
        if line == "\n":
            cases.append(case)
            case = []
        
        else:
            case.append(line.rstrip().split())
    cases.append(case) 

    return cases

if __name__ == "__main__":

    cases = get_cases('casos_de_teste.txt')
