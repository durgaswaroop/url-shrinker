class UrlsController < ApplicationController
  def create
    # Create a new url object from the parameters dictionary
    puts @url
    @url = Url.new(url_params)
  end

  # Url params.
  private
  def url_params
    params.require(:url).permit(:original)
  end

end
