#include <stdio.h>
void main()
{
	FILE* fp;
	int num;
	int *p = &num;
	int i = 0;
	fp = NULL;
	fp = fopen("b.bin","rb");
	
	for(i=0;i<3;i++)
	{	
		fread(p,sizeof(int),1,fp);
		printf("%d\n",*p);
		
	}
	fclose(fp);
}