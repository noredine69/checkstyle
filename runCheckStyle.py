import os
import subprocess
import re
import array

def getdiff():
    output = subprocess.check_output(["git", "diff", "--cached", "--unified=0", "--no-color"])
    return output

def difflines(gitDiff):
    path = ""
    line = 0
    result = []
    for diff in gitDiff.splitlines():
        if (re.search('---\ (a/)?.*', diff) != None):
            continue            
        else:
            match = re.search('\+\+\+\ (b/)?(.*)', diff)
            if(match != None):
                path = match.group(2)
            else:
                match = re.search('@@\ -[0-9]+(,[0-9]+)?\ \+([0-9]+)(,[0-9]+)?\ @@.*', diff)
                if(match != None):
                    line = int(match.group(2))
                else:
                    match = re.search('^($esc\[[0-9;]+m)*([\ +-])', diff)
                    if(match != None):
                        result.append(path + ":" + str(line))
                        
                        if(match.group() != "-"):
                            line+=1
    print result

        

if __name__ == '__main__':
    diffs = getdiff()
    difflines(diffs)
