package com.krushisevakendra.service;

import com.krushisevakendra.dto.CategoryDto;
import com.krushisevakendra.entity.Category;

import java.util.List;
import java.util.Optional;

public interface CategoryService {
    List<Category> getAllActiveCategories();
    List<Category> getAllCategories();
    Optional<Category> getCategoryById(Long id);
    Category saveCategory(CategoryDto dto);
    Category updateCategory(Long id, CategoryDto dto);
    void deleteCategory(Long id);
    Category toggleCategoryStatus(Long id);
}
