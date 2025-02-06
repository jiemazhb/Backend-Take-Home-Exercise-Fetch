package com.example.receipt_processor.model;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;
import lombok.Data;

@Data
public class Item{
        @NotBlank
        @Pattern(regexp = "^[\\w\\s\\-]+$")
        private String shortDescription;
        @NotBlank
        @Pattern(regexp = "^\\d+\\.\\d{2}$")
        private String price;
}
