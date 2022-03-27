import random
import time

def main():
    try:
        code = random.randint(0,10000)
        with open('generated_code.txt', 'w') as f:
            f.write(str(code))
        #print('The code was generated')
        time.sleep(5)
        main()    
    except:
        print('Something goes wrong')
if __name__=='__main__':
    #print('Let \'s generate')
    main()
