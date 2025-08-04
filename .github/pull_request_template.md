# Pull Request Template

## Description
<!-- Provide a brief description of the changes in this PR -->

## Type of Change
<!-- Check the type of change this PR introduces -->
- [ ] 🐛 Bug fix (non-breaking change which fixes an issue)
- [ ] ✨ New feature (non-breaking change which adds functionality)
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📚 Documentation update
- [ ] 🧪 Test improvements
- [ ] 🔧 Maintenance/refactoring
- [ ] ⚡ Performance improvement

## Changes Made
<!-- List the specific changes made in this PR -->
- 
- 
- 

## Demo Type Affected
<!-- Check which demo types are affected by this change -->
- [ ] Basic Demo
- [ ] Advanced Demo
- [ ] Interactive Demo
- [ ] Real World Demo
- [ ] R&D Analytics Demo
- [ ] CLI Interface
- [ ] Package Infrastructure
- [ ] Documentation

## Testing
<!-- Describe the tests you ran to verify your changes -->
- [ ] All existing tests pass
- [ ] Added new tests for the changes
- [ ] Tested with different Python versions
- [ ] Tested CLI functionality
- [ ] Tested VS Code integration

### Test Commands Run
```bash
# Add the commands you used to test
python -m pytest tests/ -v
python run_demos.py
```

## Screenshots
<!-- If applicable, add screenshots to help explain your changes -->

## Checklist
<!-- Check off items as you complete them -->
- [ ] My code follows the project's coding standards
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published

## API Key Testing
<!-- For changes that affect API interactions -->
- [ ] Tested with valid API key
- [ ] Tested error handling for missing/invalid API key
- [ ] No API keys exposed in code or logs

## Breaking Changes
<!-- If this is a breaking change, describe what breaks and how to migrate -->

## Additional Notes
<!-- Add any additional notes, concerns, or considerations for reviewers -->

## Related Issues
<!-- Link any related issues -->
Fixes #
Relates to #

---

**Reviewer Notes:**
- Please test the changes locally before approving
- Verify that all demo types still work as expected
- Check that documentation is updated if needed
