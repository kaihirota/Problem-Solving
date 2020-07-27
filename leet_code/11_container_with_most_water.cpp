/*
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
*/

#include <iostream> // cin cout
#include <fstream> // file i/o
#include <string>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0, r = height.size() - 1, curr_area = 0, area = 0;
        while(l < r) {
            if(height[l] > height[r]) {
                area = height[r] * (r - l);
                r -= 1;
            }
            else {
                area = height[l] * (r - l);
                l += 1;
            }
            curr_area = max(curr_area, area);
        }
        return curr_area;
    }
};

int main() {
    int arr[] = { 1,8,6,2,5,4,8,3,7 };
    int n = sizeof(arr) / sizeof(arr[0]);
    vector<int> height(arr, arr + n);
    Solution solution;
    int maxArea = solution.maxArea(height);
    cout << maxArea << endl;
    return maxArea;
}
