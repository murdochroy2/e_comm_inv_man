const API_BASE_URL = 'http://localhost:8000/api';

export const categoryService = {
    getAllCategories: async () => {
        try {
            const response = await fetch(`${API_BASE_URL}/categories/`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Error fetching categories:', error);
            throw error;
        }
    },

    createCategory: async (categoryData) => {
        try {
            const response = await fetch(`${API_BASE_URL}/categories/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(categoryData)
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Error creating category:', error);
            throw error;
        }
    },

    deleteCategory: async (categoryId) => {
        try {
            const response = await fetch(`${API_BASE_URL}/categories/${categoryId}/`, {
                method: 'DELETE'
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return true; // Since DELETE typically doesn't return data
        } catch (error) {
            console.error('Error deleting category:', error);
            throw error;
        }
    }
};

export const productService = {
    getAllProducts: async () => {
        try {
            const response = await fetch(`${API_BASE_URL}/products/`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Error fetching products:', error);
            throw error;
        }
    },

    createProduct: async (productData) => {
        try {
            const response = await fetch(`${API_BASE_URL}/products/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(productData)
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Error creating product:', error);
            throw error;
        }
    },

    deleteProduct: async (productId) => {
        try {
            const response = await fetch(`${API_BASE_URL}/products/${productId}/`, {
                method: 'DELETE'
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return true;
        } catch (error) {
            console.error('Error deleting product:', error);
            throw error;
        }
    }
}; 