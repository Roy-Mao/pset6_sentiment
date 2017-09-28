import argparse;
import string;
import crypt;
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("given_pw", help = "give me the password to decrypt.")
    args = parser.parse_args()
    my_list = list(string.ascii_letters);
    for a in range(52):
        guess_str = my_list[a]
        guess_pw = crypt.crypt(guess_str, "50")
        if guess_pw == args.given_pw:
            print("Match found, and the password should be {}".format(guess_str))
            return
        
    for a in range(52):
        for b in range(52):
            guess_str = my_list[a] + my_list[b]
            guess_pw = crypt.crypt(guess_str, "50")
            if guess_pw == args.given_pw:
                print("Match found, and the password should be {}".format(guess_str))
                return
            
    for a in range(52):
        for b in range(52):
            for c in range(52):
                guess_str = my_list[a] + my_list[b] + my_list[c]
                guess_pw = crypt.crypt(guess_str, "50")
                if guess_pw == args.given_pw:
                    print("Match found, and the password should be{}".format(guess_str))
                    return
                
    for a in range(52):
        for b in range(52):
            for c in range(52):
                for d in range(52):
                    guess_str = my_list[a] + my_list[b] + my_list[c] + my_list[d]
                    guess_pw = crypt.crypt(guess_str, "50")
                    if guess_pw == args.given_pw:
                        print("Match found, and the password should be {}".format(guess_str))
                        return
                    
    print ("Sorry, no match found.")
    return
        
    
    
    
if __name__ == "__main__":
    main()
    
    
    