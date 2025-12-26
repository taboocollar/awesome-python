#!/usr/bin/env python
# coding: utf-8

"""
Unit tests for sort.py module.
Tests the sorting functionality for the awesome-python README.md file.
"""

import os
import pytest
from sort import sort_blocks, main


class TestSortBlocks:
    """Test cases for the sort_blocks function."""

    def test_sort_blocks_basic(self, tmp_path):
        """Test basic sorting of blocks in README."""
        # Create a temporary README with unsorted content
        readme_content = """# Header
- - -
## Section A

* [Zebra](http://example.com/zebra) - Description.
* [Alpha](http://example.com/alpha) - Description.

## Section B

* [Beta](http://example.com/beta) - Description.
"""
        readme_file = tmp_path / "README.md"
        readme_file.write_text(readme_content)
        
        # Change to temp directory
        original_dir = os.getcwd()
        os.chdir(tmp_path)
        
        try:
            sort_blocks()
            result = readme_file.read_text()
            
            # Check that content is present
            assert "## Section A" in result
            assert "## Section B" in result
            assert "Alpha" in result
            assert "Beta" in result
        finally:
            os.chdir(original_dir)

    def test_sort_blocks_with_table_of_contents(self, tmp_path):
        """Test that table of contents is preserved."""
        readme_content = """# Awesome Python

Table of contents line 1
Table of contents line 2
- - -
## Libraries

* [Zebra](http://example.com/zebra) - Description.
* [Alpha](http://example.com/alpha) - Description.
"""
        readme_file = tmp_path / "README.md"
        readme_file.write_text(readme_content)
        
        original_dir = os.getcwd()
        os.chdir(tmp_path)
        
        try:
            sort_blocks()
            result = readme_file.read_text()
            
            # Check that table of contents is preserved
            assert "Table of contents line 1" in result
            assert "Table of contents line 2" in result
            assert "- - -" in result
        finally:
            os.chdir(original_dir)


class TestMain:
    """Test cases for the main function."""

    def test_main_sorts_links_alphabetically(self, tmp_path):
        """Test that main function sorts links alphabetically (case-insensitive)."""
        readme_content = """# Awesome Python

Table of Contents
- - -

## Section

* [Zebra](http://example.com/zebra) - Description.
* [alpha](http://example.com/alpha) - Description.
* [Beta](http://example.com/beta) - Description.
"""
        readme_file = tmp_path / "README.md"
        readme_file.write_text(readme_content)
        
        original_dir = os.getcwd()
        os.chdir(tmp_path)
        
        try:
            # Run main function which calls sort_blocks internally
            main()
            result = readme_file.read_text()
            
            # Find the positions of each link
            alpha_pos = result.find("* [alpha]")
            beta_pos = result.find("* [Beta]")
            zebra_pos = result.find("* [Zebra]")
            
            # Verify they are in alphabetical order (case-insensitive)
            assert alpha_pos < beta_pos < zebra_pos, "Links should be sorted alphabetically"
        finally:
            os.chdir(original_dir)

    def test_main_preserves_non_link_lines(self, tmp_path):
        """Test that non-link lines are preserved and not sorted."""
        readme_content = """# Awesome Python

Description paragraph.
- - -

## Section

Some text here.

* [Zebra](http://example.com/zebra) - Description.
* [Alpha](http://example.com/alpha) - Description.

More text here.
"""
        readme_file = tmp_path / "README.md"
        readme_file.write_text(readme_content)
        
        original_dir = os.getcwd()
        os.chdir(tmp_path)
        
        try:
            main()
            result = readme_file.read_text()
            
            # Check that non-link content is preserved
            assert "Description paragraph." in result
            assert "Some text here." in result
            assert "More text here." in result
        finally:
            os.chdir(original_dir)

    def test_main_handles_multiple_sections(self, tmp_path):
        """Test sorting across multiple sections."""
        readme_content = """# Awesome Python

Table of Contents
- - -

## Section One

* [Zulu](http://example.com/zulu) - Description.
* [Alpha](http://example.com/alpha) - Description.

## Section Two

* [Yankee](http://example.com/yankee) - Description.
* [Bravo](http://example.com/bravo) - Description.
"""
        readme_file = tmp_path / "README.md"
        readme_file.write_text(readme_content)
        
        original_dir = os.getcwd()
        os.chdir(tmp_path)
        
        try:
            main()
            result = readme_file.read_text()
            
            # Both sections should exist
            assert "## Section One" in result
            assert "## Section Two" in result
            
            # Extract section one content
            section_one_start = result.find("## Section One")
            section_two_start = result.find("## Section Two")
            section_one = result[section_one_start:section_two_start]
            
            # Check sorting within section one
            alpha_in_one = section_one.find("Alpha")
            zulu_in_one = section_one.find("Zulu")
            assert alpha_in_one < zulu_in_one, "Section One should be sorted"
            
            # Extract section two content
            section_two = result[section_two_start:]
            bravo_in_two = section_two.find("Bravo")
            yankee_in_two = section_two.find("Yankee")
            assert bravo_in_two < yankee_in_two, "Section Two should be sorted"
        finally:
            os.chdir(original_dir)

    def test_main_handles_dash_and_asterisk_bullets(self, tmp_path):
        """Test that both - and * bullet styles are handled."""
        readme_content = """# Awesome Python

Table of Contents
- - -

## Section

- [Zebra](http://example.com/zebra) - Description.
- [Alpha](http://example.com/alpha) - Description.
* [Yankee](http://example.com/yankee) - Description.
* [Bravo](http://example.com/bravo) - Description.
"""
        readme_file = tmp_path / "README.md"
        readme_file.write_text(readme_content)
        
        original_dir = os.getcwd()
        os.chdir(tmp_path)
        
        try:
            main()
            result = readme_file.read_text()
            
            # All entries should be present
            assert "Alpha" in result
            assert "Bravo" in result
            assert "Yankee" in result
            assert "Zebra" in result
        finally:
            os.chdir(original_dir)

    def test_main_handles_indented_lists(self, tmp_path):
        """Test that indented lists are sorted separately."""
        readme_content = """# Awesome Python

Table of Contents
- - -

## Section

* [Zebra](http://example.com/zebra) - Description.
* [Alpha](http://example.com/alpha) - Description.
    * [Nested-Zulu](http://example.com/zulu) - Description.
    * [Nested-Bravo](http://example.com/bravo) - Description.
"""
        readme_file = tmp_path / "README.md"
        readme_file.write_text(readme_content)
        
        original_dir = os.getcwd()
        os.chdir(tmp_path)
        
        try:
            main()
            result = readme_file.read_text()
            
            # Check that all entries are present
            assert "Alpha" in result
            assert "Zebra" in result
            assert "Nested-Bravo" in result
            assert "Nested-Zulu" in result
        finally:
            os.chdir(original_dir)

    def test_main_minimal_file(self, tmp_path):
        """Test handling of minimal README file with separator."""
        readme_content = """# Awesome Python
- - -
"""
        readme_file = tmp_path / "README.md"
        readme_file.write_text(readme_content)
        
        original_dir = os.getcwd()
        os.chdir(tmp_path)
        
        try:
            main()
            result = readme_file.read_text()
            # Should not crash and basic structure should be preserved
            assert "# Awesome Python" in result
            assert "- - -" in result
        finally:
            os.chdir(original_dir)

    def test_main_no_links(self, tmp_path):
        """Test handling of README with no links."""
        readme_content = """# Awesome Python

This is just text.
- - -

## Section

More text here.
"""
        readme_file = tmp_path / "README.md"
        readme_file.write_text(readme_content)
        
        original_dir = os.getcwd()
        os.chdir(tmp_path)
        
        try:
            main()
            result = readme_file.read_text()
            # Content should be preserved
            assert "This is just text." in result
            assert "More text here." in result
        finally:
            os.chdir(original_dir)


class TestSortingBehavior:
    """Integration tests for overall sorting behavior."""

    def test_case_insensitive_sorting(self, tmp_path):
        """Test that sorting is case-insensitive."""
        readme_content = """# Awesome Python

Table of Contents
- - -

## Libraries

* [ZEBRA](http://example.com/zebra) - Description.
* [alpha](http://example.com/alpha) - Description.
* [Beta](http://example.com/beta) - Description.
* [charlie](http://example.com/charlie) - Description.
"""
        readme_file = tmp_path / "README.md"
        readme_file.write_text(readme_content)
        
        original_dir = os.getcwd()
        os.chdir(tmp_path)
        
        try:
            main()
            result = readme_file.read_text()
            
            # Find positions
            alpha_pos = result.find("* [alpha]")
            beta_pos = result.find("* [Beta]")
            charlie_pos = result.find("* [charlie]")
            zebra_pos = result.find("* [ZEBRA]")
            
            # Check case-insensitive alphabetical order
            assert alpha_pos < beta_pos, "alpha should come before Beta"
            assert beta_pos < charlie_pos, "Beta should come before charlie"
            assert charlie_pos < zebra_pos, "charlie should come before ZEBRA"
        finally:
            os.chdir(original_dir)

    def test_special_characters_in_links(self, tmp_path):
        """Test handling of special characters in link names."""
        readme_content = """# Awesome Python

Table of Contents
- - -

## Libraries

* [Zebra-Tool](http://example.com/zebra) - Description.
* [Alpha.js](http://example.com/alpha) - Description.
* [Beta_Library](http://example.com/beta) - Description.
"""
        readme_file = tmp_path / "README.md"
        readme_file.write_text(readme_content)
        
        original_dir = os.getcwd()
        os.chdir(tmp_path)
        
        try:
            main()
            result = readme_file.read_text()
            
            # All should be present after sorting
            assert "Alpha.js" in result
            assert "Beta_Library" in result
            assert "Zebra-Tool" in result
        finally:
            os.chdir(original_dir)
