#include <iostream>
#include <fstream>

#define FILE_P "d2.gtf"
#define FLIE_S "../../ref/GCF_000750555.1_ASM75055v1_genomic.fna"

int EXTEND=30;

int main(){
    std::ifstream fs(FLIE_S);
    std::ifstream fp(FILE_P);
    char buffer;
    int p=1;
    int start;
    int end;


    std::string head;
    std::getline(fs, head);

    fp>>start;
    fp>>end;

    start-=EXTEND;
    end+=EXTEND;

    while (!fs.eof()){
        fs>>buffer;
        if(p>=start && p<=end)
            std::cout<<buffer;
        if(p>end){
            if(fp.eof())
                break;
            std::cout<<std::endl;
            fp>>start;
            fp>>end;
            start-=EXTEND;
            end+=EXTEND;
        }
        ++p;
    }
}