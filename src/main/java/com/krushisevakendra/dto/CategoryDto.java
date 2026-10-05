package com.krushisevakendra.dto;

import jakarta.validation.constraints.NotBlank;
import org.springframework.web.multipart.MultipartFile;

public class CategoryDto {

    private Long id;

    @NotBlank(message = "Category name is required / वर्गाचे नाव आवश्यक आहे")
    private String name;

    private String nameMr;
    private String description;
    private String status = "ACTIVE";
    private String existingImage;
    private MultipartFile imageFile;

    public CategoryDto() {}

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getNameMr() {
        return nameMr;
    }

    public void setNameMr(String nameMr) {
        this.nameMr = nameMr;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getExistingImage() {
        return existingImage;
    }

    public void setExistingImage(String existingImage) {
        this.existingImage = existingImage;
    }

    public MultipartFile getImageFile() {
        return imageFile;
    }

    public void setImageFile(MultipartFile imageFile) {
        this.imageFile = imageFile;
    }
}
