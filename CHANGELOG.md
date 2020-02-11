# v5.1.0 (31 Jan 2020)

### Feature

* add hierarchical inspection classes (0d746594d9d14e23b7d90b359c8869b8d3ab7afc)
  Useful for extension points and caluma-as-django-app

### Fix

* validation performance vastly improved (25570a9b220d773b5a1517bb4e0b40d27ed306f1)
  form validation query count is roughly 10% of what it used to be


# v5.0.0 (22 Jan 2020)


### Feature
* add assigned users filter (93badb4a55e91f7ffc6a3fc5828b18765cae9564)
* prefix all apps with "caluma_" (928146577f3cb2f76a4e715ba29ae4e1eb547907)
  (BREAKING CHANGE: Extension code must be updated)

### Fix
* correctly handle indirectly hidden questions (cfe616684980d732fe667099a74461d6dbfaa732)
* version bump (d2a4755c4e06d7f683165e582780ec3e5121c835)

### Documentation
* add maintainer's handbook (9f64fc4837bb5974fb7cd3caa67bb6c32bf2661e)


# v4.3.0 (18 Dec 2019)

### Feature
* make caluma installable as django app (573e87a76ca3a2b70816ce98fd08c2cc71fc5c74)


# v4.2.0 (17 Dec 2019)

### Feature
* helper to extract mutation parameters from request (197a775d332576b03853ded00c80c3abf46f4f25)
* run pytest in parallel with xdist (9a435d9d0714aef64b955c2942803a17e561a721)
* allow filtering answers to limit only visible answers (0eb037f8d1a09a7a752ac6bec58e9f4a70a17bdc)
* add pipenv setup command to setup.py (448b821ab557e0af59fcab3a976c0e00a5e98e82)

### Fix
* use root form as form property in QuestionJexl context (5f422c01cb42d0d2833f79774eb34cd4fbbdb85a)
* remove insignificant performance hack (db3d84234fa2d803f51ac3c892abba17d7c91614)
* use "development" instead of "dev" as documented (1645ed996d4f310a91fb893627158945fbbedcc3)

### Documentation
* add info about the `UID` variable (f9a8d3ffee95b39474f31dd8d79d126ff6fde006)
* add more detailed example for the pipenv workflow (16a94a81582b4164280157f559236d009ed4461d)


# v4.1.0 (28 Nov 2019)

### Feature
* make permission decorators chainable
(3052cbff33cb98ee22a7ed34c3133820121794bf)

### Fix
* validate dependencies correctly (854f6fa77048edeb9bc84d24036fff4fde2f05de)

# v4.0.0 (21 Nov 2019)

### Feature
* add created_at, closed_at, modified_at filters to work items (b83ce9c6b0b8248b82216e30c65ecb400660fdc4)

### Fix
* optimize `historical_qs_as_of` (95e5fb9865d523e0acf96c54743cebf70b6344a9)
* fix duplicate documents (68934392c56e2d1734a5046e7e5182e07ce3fd0e)
* use LocalizedValue for translations (3cf3720f94ed64367c55b700be97a955472b00e4)
* correctly handle is_hidden regarding dependencies (a068c2c04b94f94b25087c769a931ce8f549251f)

### Breaking
* allow Answers with empty value (81cbe9aae553ed91a86c1813a47085fb3b386713)

### Documentation
* explain how to use pipenv (745380f39b45fdf1d936aad87a368c2b37e75109)


# v3.0.0 (6 Nov 2019)

Version 3.0.0. Main changes:

* License changed to GPL 3.0 (or later)
* Dynamic data source improvements (Answers now store values for the case where the value won't be available in the future anymore)
* Allow skipping of work items

### Feature
* allow skipping of work items (e84f9360cb245587dab7e75d84134b7999bfa2e5)
* add `status_skipped` to possible `workitem` states (c3d99bc9d911a103796821e09f3f65bb543457ca)
* switch main license to GPL-3.0-or-later (978f18aaa725ad779bd0238b82528401f36147bb)
* implement dynamic data source (63ffe863bd17cc75c75d7834e7f38e45268022da)

### Fix
* question id/slug should be of type id (69511c17cccba36775840976d384010867256499)
* add user and group to dynamic option (ba89f88b7cec45b17e0c6036884998cdad873f0f)
* raise a 401 if user is not logged in (1b5851c2025d1e3b95353f71d2678f640847955e)
* add question to validate_answer_value method (3667e3d3aaf45459135718c401e40c02535adc01)
* fix DynamicOption model (35935ddd04861a7c2c9cc0ec8aa92de983f1c334)
* do not return questions multiple times (ec285957c661b04ed10f305fbae7b6824cfd4b97)
* remove dynamicoptionSet form schema (0391c04481097792ef608afdebb6f39d10077959)
* reintroduce ordering by deadline on work items (fed67da288aebff593cc77855b1b5c39f44d0b91)
* fix ordering by question value (1dcec885518d6f654773e07677cb58649613ede2)
* revert dynamic data source (85fab681039f5f11c484a3c525631af6e0eddd25)
* validate requiredness recursively for subforms (844b914f98f1ed002f9dbbabffaf445753a18728)
* do not validate hidden questions (1fb7bd5b93368c0c5c55bbc6e941f8208aeb2929)

### Breaking
* Add the parameter `question` to the `validate_answer_value`method and add a new lookup to check if a `dynamic_option` already exists.  (3667e3d3aaf45459135718c401e40c02535adc01)
* The `value` field on the `DynamicOption` model is renamed to `slug` and not optional anymore.  (35935ddd04861a7c2c9cc0ec8aa92de983f1c334)
* The optional `answer_value` parameter for the `DataSource.get_data()` method was reverted.  (85fab681039f5f11c484a3c525631af6e0eddd25)

### Documentation
* explain license choice (4d59af520da53b44c3771eb53c451d209c1aafa5)


# v3.0.0a1 (6 Nov 2019)

### Feature
* allow skipping of work items (e84f9360cb245587dab7e75d84134b7999bfa2e5)
* add `status_skipped` to possible `workitem` states (c3d99bc9d911a103796821e09f3f65bb543457ca)
* switch main license to GPL-3.0-or-later (978f18aaa725ad779bd0238b82528401f36147bb)
* implement dynamic data source (63ffe863bd17cc75c75d7834e7f38e45268022da)

### Fix
* add user and group to dynamic option (ba89f88b7cec45b17e0c6036884998cdad873f0f)
* raise a 401 if user is not logged in (1b5851c2025d1e3b95353f71d2678f640847955e)
* add question to validate_answer_value method (3667e3d3aaf45459135718c401e40c02535adc01)
* fix DynamicOption model (35935ddd04861a7c2c9cc0ec8aa92de983f1c334)
* do not return questions multiple times (ec285957c661b04ed10f305fbae7b6824cfd4b97)
* remove dynamicoptionSet form schema (0391c04481097792ef608afdebb6f39d10077959)
* reintroduce ordering by deadline on work items (fed67da288aebff593cc77855b1b5c39f44d0b91)
* fix ordering by question value (1dcec885518d6f654773e07677cb58649613ede2)
* revert dynamic data source (85fab681039f5f11c484a3c525631af6e0eddd25)
* validate requiredness recursively for subforms (844b914f98f1ed002f9dbbabffaf445753a18728)
* do not validate hidden questions (1fb7bd5b93368c0c5c55bbc6e941f8208aeb2929)

### Breaking
* Add the parameter `question` to the `validate_answer_value`method and add a new lookup to check if a `dynamic_option` already exists.  (3667e3d3aaf45459135718c401e40c02535adc01)
* The `value` field on the `DynamicOption` model is renamed to `slug` and not optional anymore.  (35935ddd04861a7c2c9cc0ec8aa92de983f1c334)
* The optional `answer_value` parameter for the `DataSource.get_data()` method was reverted.  (85fab681039f5f11c484a3c525631af6e0eddd25)

### Documentation
* explain license choice (4d59af520da53b44c3771eb53c451d209c1aafa5)

# v2.0.0 (18 October 2019)

This is the second major release of Caluma.

Apart from a couple of new features, we changed the license from MIT to AGPL.
The reasons for this are documented in a followup (see #749).

There's another backwards-incompatible change regarding the data sources for
dynamic (multiple) choice questions, prompting the version bump.

New in this version is also the separation between ordering and filtering in the queries,
and a cleanup command for historical data.

### Feature
* pass actual answer value to data source (3b26162db5bfd0b48b908ef7609abeddcf24af8b)
* add order filter for workflow models too (b2fb9c73d451d2292e2bdafa25b9da1151d0915b)
* add test for new order filters (344bc9d502469acc5597355d1b832e68b5893e11)
* introduce new-style ordering for form nodes (f73f8e5a6c3d287804dca88da636c515c26b2026)
* implement new order filter (012d1f19089dff4bb0125d982cc6688374e4f68a)
* start using the collection filterset factory (97394c7e523f40af102828c94dd01de7c3a97f7a)
* factory for unionized filters (686484d1e732828db2e55b7056a83925104da676)
* expose original document id (051cf01ed283dbc8b3c00a91f9a124a764f9d755)
* add cleanup command (a66582a4945c3562828cdca284e3fff8da11af98)

### Fix
* typo (9cd21c195383ec3642a0e1bc5ef2cc46c1f269ef)
* link guide (57df4a6dc35c54aa32bfb1eccef64465191f2b4a)
* don't pass self to super().__init__() call (748c99d6315d99551f9e950b3888cafd321b8b58)
* correct svg font (576e2fe71a5562f1c41fdce83ab926be0ecbab45)
* cleanup_history - add force argument (9191b4e3638f866d256ac3b40a59b6839a6d4ef5)

### Breaking
* `DataSource.get_data()` methods must accept an optional `answer_value` parameter.  (3b26162db5bfd0b48b908ef7609abeddcf24af8b)
* License change: Move to AGPL (bfb66199)

### Documentation
* update ordering documentation (85a1143b02884f75fd3c24fccfa842c5f783adf6)
* add note on deprecation of old-style filters (b93e27c49f5b57d0acbdd560766ddff2baefc041)
* extend the guide with form-builder steps (bdd183d111e844e739c74d0536d2c4e29aec7b39)
* add guide (WIP) (822f4c1c31ee3f404b5c4b9cc76d96e2a1be1a5f)
* document cleanup commands in README (dc58593af1d147bd06cb62b02f2d27459cc7f01e)


# v1.0.0 (25 September 2019)

Initial release