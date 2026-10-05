package com.krushisevakendra.service.impl;

import com.krushisevakendra.dto.CategoryDto;
import com.krushisevakendra.entity.Category;
import com.krushisevakendra.exception.ResourceNotFoundException;
import com.krushisevakendra.repository.CategoryRepository;
import com.krushisevakendra.service.CategoryService;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Service
@Transactional
public class CategoryServiceImpl implements CategoryService {

    private final CategoryRepository categoryRepository;

    public CategoryServiceImpl(CategoryRepository categoryRepository) {
        this.categoryRepository = categoryRepository;
    }

    @Override
    @Transactional(readOnly = true)
    public List<Category> getAllActiveCategories() {
        return categoryRepository.findByStatusOrderByNameAsc("ACTIVE");
    }

    @Override
    @Transactional(readOnly = true)
    public List<Category> getAllCategories() {
        return categoryRepository.findAll();
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Category> getCategoryById(Long id) {
        return categoryRepository.findById(id);
    }

    @Override
    public Category saveCategory(CategoryDto dto) {
        Category category = new Category();
        category.setName(dto.getName().trim());
        category.setNameMr(dto.getNameMr() != null ? dto.getNameMr().trim() : null);
        category.setDescription(dto.getDescription());
        category.setImage(dto.getExistingImage() != null ? dto.getExistingImage() : "category_default.jpg");
        category.setStatus(dto.getStatus() != null ? dto.getStatus() : "ACTIVE");
        category.setCreatedAt(LocalDateTime.now());
        return categoryRepository.save(category);
    }

    @Override
    public Category updateCategory(Long id, CategoryDto dto) {
        Category category = categoryRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Category not found with id: " + id));

        category.setName(dto.getName().trim());
        category.setNameMr(dto.getNameMr() != null ? dto.getNameMr().trim() : null);
        category.setDescription(dto.getDescription());
        if (dto.getExistingImage() != null && !dto.getExistingImage().isBlank()) {
            category.setImage(dto.getExistingImage());
        }
        if (dto.getStatus() != null) {
            category.setStatus(dto.getStatus());
        }
        return categoryRepository.save(category);
    }

    @Override
    public void deleteCategory(Long id) {
        if (!categoryRepository.existsById(id)) {
            throw new ResourceNotFoundException("Category not found with id: " + id);
        }
        categoryRepository.deleteById(id);
    }

    @Override
    public Category toggleCategoryStatus(Long id) {
        Category category = categoryRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Category not found with id: " + id));
        category.setStatus("ACTIVE".equalsIgnoreCase(category.getStatus()) ? "INACTIVE" : "ACTIVE");
        return categoryRepository.save(category);
    }
}
