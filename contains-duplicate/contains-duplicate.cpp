#include <stdio.h>
#include <assert.h>
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        for (int i : nums) {
            if (s.count(i) > 0) {
                return true;
            }
            s.insert(i);
        }
        return false;
    }
};


int main(void) {
    Solution sol = Solution();
    vector<int> t1{ 1,2,3,1 };
    assert(sol.containsDuplicate(t1));

    vector<int> t2{ 1,2,3,4 };
    assert(!sol.containsDuplicate(t2));

    return 0;
}
