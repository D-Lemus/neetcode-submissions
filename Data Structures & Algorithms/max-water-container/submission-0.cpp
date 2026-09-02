class Solution {
public:
    int maxArea(vector<int>& heights) {
        
        int biggest_cont = 0;
        int r = heights.size()-1;
        int l=0;
        while(r > l)
        {
            int width = r - l;
            int height = min(heights[l],heights[r]);
            int area = width * height;

            if(area > biggest_cont) biggest_cont = area;

            if(heights[l] > heights[r])  r--;
            else l++;

            
        }
        return biggest_cont;
    }
};
