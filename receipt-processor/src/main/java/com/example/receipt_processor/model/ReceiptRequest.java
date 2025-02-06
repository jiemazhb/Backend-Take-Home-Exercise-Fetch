package com.example.receipt_processor.model;

import jakarta.validation.Valid;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;
import jakarta.validation.constraints.Size;
import lombok.Data;
import org.springframework.format.annotation.DateTimeFormat;

import java.util.List;

@Data
public class ReceiptRequest{
    @NotBlank
    @Pattern(regexp = "^[\\w\\s\\-&]+$")
    private String retailer;
    @NotBlank
    @Pattern(regexp = "^\\d{4}-\\d{2}-\\d{2}$")
    private String purchaseDate;
    @NotBlank
    @Pattern(regexp = "^([01]?\\d|2[0-3]):[0-5]\\d$")
    private String purchaseTime;
    @Valid
    @Size(min = 1)
    private List<Item> items;
    @NotBlank
    @Pattern(regexp = "^\\d+\\.\\d{2}$")
    private String total;
}
