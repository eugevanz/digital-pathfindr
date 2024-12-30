# from typing import List, Optional
#
# from pydantic import BaseModel
# from webflow import Field, Collection, Pagination, Page, Site
#
#
# class CustomDomain(BaseModel):
#     id: str
#     url: str
#
#
# class Locale(BaseModel):
#     id: str
#     cmsLocaleId: str
#     enabled: bool
#     displayName: str
#     redirect: bool
#     subdirectory: str
#     tag: str
#
#
# class Locales(BaseModel):
#     primary: Locale
#     secondary: Optional[List[Locale]]
#
#
# class SitesResponse(BaseModel):
#     sites: List[Site]
#
#
# class PagesResponse(BaseModel):
#     pages: List[Page]
#     pagination: Pagination
#
#
# class CollectionsResponse(BaseModel):
#     collections: List[Collection]
#
#
# class CollectionDetails(BaseModel):
#     id: str
#     fields: List[Field]
#     displayName: str
#     singularName: str
#     slug: str
#     createdOn: str
#     lastUpdated: str
