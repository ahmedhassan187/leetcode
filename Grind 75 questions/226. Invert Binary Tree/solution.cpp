class Solution {
public:
    void swap(TreeNode* root){
        if (!root){
            return;
        }
        swap(root->left);
        swap(root->right);
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
    }
    TreeNode* invertTree(TreeNode* root) {
        swap(root);
        return root;
    }
};
