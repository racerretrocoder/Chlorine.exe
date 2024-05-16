#include <iostream> 
#include <windows.h> // WinApi header 

using namespace std;

int main() 
{ 
    

    Beep(493,200); // 493 hertz (B4) for 500 milliseconds     

    while (true)
		{
      Beep(493,300); // 493 hertz (B4) for 500 milliseconds 
    MessageBox(NULL, "IM GOING TO CRASH YOUR COMPUTER HAHAHAHAH", "BSOD.EXE's REVENGE", MB_ICONERROR); 
		}

   // cin.get(); // wait 
    return 0; 
}