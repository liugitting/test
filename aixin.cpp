#include <stdio.h>
#include <windows.h>
#include <iostream>
using namespace std;

int main()
{
    float x, y, a;
    for (y = 1.5f; y > -1.5f; y -= 0.1f)
    {
        /* code */
        for (x = -1.5f; x < 1.5f; x += .05f)
        {
            /* code */
            a = x * x + y * y - 1;
            putchar(a * a * a - x * x * y * y * y < 0.0f ? 'x' : ' ');
        }
        Sleep(100);
        putchar('\n');
    }
    cout << "Press any key to exit" << endl;
    getchar();
    return 0;
}