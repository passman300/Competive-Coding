#include <bits/stdc++.h>
using namespace std;
const int MM = 1003;

int T;
int N, K;


int painting[MM][MM];
int stamp[MM][MM];
int tempCanvas[MM][MM];

void rotate()
{
    for (int i = 1; i <= K; i++)
    {
        for (int j = i; j <= K; j++)
        {
            swap(stamp[i][j], stamp[j][i]);
        }
    }

    for(int i = 1; i <= K; i++) {
        int left = 1, right = K;
        while(left < right) {
            swap(stamp[i][left], stamp[i][right]);
            left++;
            right--;
        }
    }
}

bool valid()
{
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            if (tempCanvas[i][j] != painting[i][j])
                return false;
        }
    }
    return true;
}

void printTempCanvas()
{
    cout << "TEMP" << endl;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            cout << tempCanvas[i][j] << " ";
        }
        cout << endl;
    }
}


int main(){
    cin.sync_with_stdio(0);
    cin.tie(0);

    cin >> T;
    int cnt = 0;
    while (cnt < T)
    {
        cin >> N;
        memset(painting, 0, sizeof(painting));
        memset(stamp, 0, sizeof(stamp));
        memset(tempCanvas, 0, sizeof(tempCanvas));

        for (int i = 1; i <= N; i++)
        {
            for (int j = 1; j <= N; j++)
            {
                char temp;
                int temp2;
                cin >> temp;
                if (temp == '.') temp2 = 0;
                else temp2 = 1;
                painting[i][j] = temp2;
            }
        }
        cin >> K;
        for (int i = 1; i <= K; i++)
        {
            for (int j = 1 ; j <= K; j++)
            {
                char temp;
                int temp2;
                cin >> temp;
                if (temp == '.') temp2 = 0;
                else temp2 = 1;

                stamp[i][j] = temp2;
            }
        }

        for (int r = 0; r < 4; r++)
        {
            // bruteforce locations of stamps
            for (int i = 1; i <= N - K + 1; i++)
            {
                for (int j = 1; j <= N - K + 1; j++)
                {
                    // check if the stamp locations are correct
                    bool flag = true;
                    for (int g = 1; g <= K ; g++)
                    {
                        for (int h = 1; h <= K ; h++)
                        {
                            if (stamp[g][h] == 1 && painting[i + g - 1][j + h - 1] == 0 && flag)
                            {
                                flag = false;
                                break;
                            }
                        }
                    }

                    if (flag)
                    {
                        for (int x = 1; x <= K; x++)
                        {
                            for (int y = 1; y <= K; y++)
                            {
                                if (stamp[x][y] == 1 && painting[i + x - 1][j + y - 1] == 1)
                                {
                                    tempCanvas[i + x - 1][j + y - 1] = 1;
                                }
                            }
                        }
                    }
                }
            }

//            printTempCanvas();


            //rotate
            rotate();

        }
//        cout << "PAINT" << endl;
//        for (int i = 1; i <= N; i++)
//        {
//            for (int j = 1; j <= N; j++)
//            {
//                cout << painting[i][j] << " ";
//            }
//            cout << endl;
//        }

        if (valid())
        {
            cout << "YES" << endl;
        }
        else cout << "NO" << endl;




        cnt++;
    }



}