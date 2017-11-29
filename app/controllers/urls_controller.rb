require 'digest'

class UrlsController < ApplicationController
  def create
    # First check if the same url already exists
    existing = Url.find_by_original(url_params[:original])

    # If the record already exists in DB, then just return
    if existing
      puts existing.shrunken
      return
    end

    # Create a new url object from the parameters dictionary
    @url = Url.new(url_params)

    # Add the shrunken url to the object
    @url.shrunken = shrink_it(@url.original)

    # Save the object to db
    if @url.save
      puts 'url saved in DB'
    end
  end

  # Url params.
  private
  def url_params
    params.require(:url).permit(:original)
  end

  def shrink_it(original_url)
    md5 = Digest::MD5.new
    # Take first 6 characters of the hash
    shrunk_hash = md5.update(original_url).base64digest[0,6]
    puts shrunk_hash
    shrunk_hash
  end

end
