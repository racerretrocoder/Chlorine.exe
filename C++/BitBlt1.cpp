#include <windows.h>

int main()
{
	{
		HDC hdc = GetDC(0);
		INT sw = GetSystemMetrics(0);
		INT sh = GetSystemMetrics(1);
		while (true)
		{
			SelectObject(hdc, CreateSolidBrush (RGB(rand() % 123, rand() % 431, rand() % 311)));
			BitBlt(hdc , rand() % 21 - 10, rand() % 21 - 10, sw, sh, hdc, 0, 0, 0x9273ecef);
			BitBlt(hdc , rand() % 21 - 10, rand() % 21 - 10, sw, sh, hdc, 0, 0, PATINVERT);
		}
	}
}